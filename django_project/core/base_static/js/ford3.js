$(document).ready(function() {
    $('#sidebar-small-link').click(function () {
        let stm = $('.small-sidebar-menu');
        if (stm.hasClass('show-sidebar-menu')) {
            stm.removeClass('show-sidebar-menu')
        }
        else {
            stm.addClass('show-sidebar-menu');
        }
    });
});
