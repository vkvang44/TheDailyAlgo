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

    });

    $("#submit-btn").click(function(){
        $(this).addClass("loading");
        $(this).val('');
    });
});


