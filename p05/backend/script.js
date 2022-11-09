$(document).ready(() => {
    $('.card').on('click', () => {
        let id = $('.card').attr('id');
        console.log(id);

        $.ajax({
            url: "./server.php",
            type: "GET",
            data: { card: id },
            success: function (response) {
                console.log('Si entro');
                console.log(response);
            },
            error: function () {
                console.log('No funcionó');
            }
        });
    });
});
