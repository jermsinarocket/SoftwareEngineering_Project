
(function ($) {
    "use strict";

    /*==================================================================
    [ Focus Contact2 ]*/
    $('[id^=id_]').keyup(function(){
        $(this).on('blur', function(){
            var thisAlert = $(this).parent();
            if($(this).val().trim() != "") {
                $(this).addClass('has-val');
                $(thisAlert).removeClass('alert-validate');
            }
            else {
                $(this).removeClass('has-val');
                $(thisAlert).addClass('alert-validate');
            }
        })
    })


})(jQuery);
