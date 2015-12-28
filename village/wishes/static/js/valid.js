$(document).on('submit', 'form[method="POST"]', function(e){
    e.preventDefault();

    // целевая форма
    var $form = $(this);
    var $target_btn = $(this).find("*[type=submit]:focus" );

    $.ajax({
        url: $target_btn.attr('formAction'),
        type: $form.attr('method'),
        data: $form.serialize(),
        dataType: 'json',

        success: function(json){
            // обрабатываем редиректы
            if (json.redirect_url) {
                window.location = json.redirect_url;
            }
        },
        error: function(xhr){
            // json-респонс
            var data = $.parseJSON(xhr.responseText);

            // удаляем пред. ошибки
            // FIXME - логично вынести класс в константу
            $('.ajax-errors').remove();

            // формирование вывода в DOM ошибок
            // FIXME - под этот бред нужно выделить отдельную процедуру
            if (data.hasOwnProperty("errors")) {
                $.each(data.errors, function(input_name, error) {
                    var $input = $('input[name=' + input_name + ']');

                    // отрендеренные ошибки
                    $.each($input, function(i, val) {
                        $(val).addClass('error').attr('title', error).tooltipster({
                            position: 'right',
                            hideOnClick: true,
                            //theme: 'custom',
                            offsetY: $(val).height() / 2
                        }).tooltipster('show');
                    });
                });
            } else {
                var $input = $form;

                // отрендеренные ошибки
                $.each($input, function(i, val) {
                    $(val).addClass('error').attr('title', data.detail).tooltipster({
                        position: 'right',
                        hideOnClick: true,
                        //theme: 'custom',
                        offsetY: $(val).height() / 2
                    }).tooltipster('show');
                });
            }
        }
    });
});
