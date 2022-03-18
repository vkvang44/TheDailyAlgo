$(function () {
    $('textarea[data-editor]').each(function () {
        var textarea = $(this);

        var mode = textarea.data('editor');

        var editDiv = $('<div>', {
            'class': textarea.attr('class')
        }).insertBefore(textarea);

        textarea.css('display', 'none');
        textarea.css('visibility', 'hidden');

        var editor = ace.edit(editDiv[0]);
        editor.renderer.setShowGutter(true);
        editor.getSession().setValue(textarea.val());
        editor.getSession().setMode("ace/mode/" + mode);
        editor.setTheme("ace/theme/dreamweaver");
        editor.setOptions({
          fontSize: "12pt",
          fontFamily: "Monospace"
        });

        // copy back to textarea on form submit...
        textarea.closest('form').submit(function () {
            textarea.val(editor.getSession().getValue());
        })

        // This function gets cookie with a given name
        function getCookie(name) {
            var cookieValue = null;
            if (document.cookie && document.cookie != '') {
                var cookies = document.cookie.split(';');
                for (var i = 0; i < cookies.length; i++) {
                    var cookie = jQuery.trim(cookies[i]);
                    // Does this cookie string begin with the name we want?
                    if (cookie.substring(0, name.length + 1) == (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        }
        var csrftoken = getCookie('csrftoken');

        /*
        The functions below will create a header with csrftoken
        */

        function csrfSafeMethod(method) {
            // these HTTP methods do not require CSRF protection
            return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
        }
        function sameOrigin(url) {
            // test that a given url is a same-origin URL
            // url could be relative or scheme relative or absolute
            var host = document.location.host; // host + port
            var protocol = document.location.protocol;
            var sr_origin = '//' + host;
            var origin = protocol + sr_origin;
            // Allow absolute or scheme relative URLs to same origin
            return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
                (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
                // or any other URL that isn't scheme relative or absolute i.e relative.
                !(/^(\/\/|http:|https:).*/.test(url));
        }

        $.ajaxSetup({
            beforeSend: function(xhr, settings) {
                if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
                    // Send the token to same-origin, relative URLs only.
                    // Send the token only if the method warrants CSRF protection
                    // Using the CSRFToken value acquired earlier
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            }
        });

        // asynchronous call when user submits code
        $('#editor-form').submit(function (e) {
            e.preventDefault();
            $.ajax({
                url: '',
                type: 'POST',
                data: {user_code: editor.getSession().getValue(), reset: false},
                success: function (response) {
                    console.log('success')
                    var std_output = response["std_output"];
                    var test_output = response["test_output"];
                    var errors = response["errors"];
    
                    //clears out the previous outputs
                    $('#test-output').empty();
                    $('#std-output').empty();
    
                    //add the new output
                    if (std_output.length > 0){
                        for (let j=0; j<std_output.length; j++) {
                            $("#std-output").append(
                                `<div id="std-output-cases-` + j + `" class="testcases"></div>`
                            )
                            for (let k=0; k<std_output[j].length; k++){
                                var name = "#std-output-cases-";
                                var num = j.toString();
                                name = name.concat(num)
                                console.log(name)
                                $(name).append(
                                    `<pre>`+ std_output[j][k] +`</pre>`
                                )
                            }
                        }
                    }
                       
                    if (test_output.length > 0) {
                        for (let j=0; j<test_output.length; j++) {
                            $("#test-output").append(
                                `<div id="test-output-cases-` + j + `" class="testcases"></div>`
                            )
                            for (let k=0; k<test_output[j].length; k++){
                                var name = "#test-output-cases-";
                                var num = j.toString();
                                name = name.concat(num)
                                console.log(name)
                                $(name).append(
                                    `<pre> `+ test_output[j][k] +`</pre>`
                                )
                            }
                        }
                    }
                        
                    if (errors != '') {
                        $("#std-output").append(
                            `<div class="testcases"><pre>`+ errors +`</pre></div>`
                        )
                    }
                        
                    $("#submit-btn").removeClass("loading")
                    $("#submit-btn").val("Run Code")
                    console.log(response)
                },
                error: function (response) {
                    // alert the error if any error occured
                    console.log('error')
                    alert(response);
                }
            })
        })

        // resets the code to initial state
        $("#reset").click(function(){
            Swal.fire({
                title: 'Are you sure?',
                text: "All code that was written will be gone.",
                icon: 'warning',
                showCancelButton: true,
                confirmButtonColor: '#3085d6',
                cancelButtonColor: '#d33',
                confirmButtonText: 'Yes',
                reverseButtons: true
              }).then((result) => {
                if (result.isConfirmed) {
                    $.ajax({
                        url: '',
                        type: 'POST',
                        data: { reset: true, },
                        success: function (response) {
                            var std_output = response["std_output"];
                            var user_code = response["user_code"];
                            editor.getSession().setValue(user_code);

                            //clears out the previous outputs
                            $('#test-output').empty();
                            $('#std-output').empty();
            
                            //add the new output
                            if (std_output.length > 0){
                                for (let j=0; j<std_output.length; j++) {
                                    $("#std-output").append(
                                        `<div id="std-output-cases-` + j + `" class="testcases"></div>`
                                    )
                                    for (let k=0; k<std_output[j].length; k++){
                                        var name = "#std-output-cases-";
                                        var num = j.toString();
                                        name = name.concat(num)
                                        $(name).append(
                                            `<pre>`+ std_output[j][k] +`<pre>`
                                        )
                                    }
                                }
                            }  
                        },
                        error: function (response) {
                            // alert the error if any error occured
                            console.log('error')
                            alert(response);
                        }
                    })
                }
              });
        })

    });

    $("#submit-btn").click(function(){
        $(this).addClass("loading");
        $(this).val('');
    });
    



   
});


