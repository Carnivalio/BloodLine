$(document).ready(function () {
    $('#myCarousel').carousel({interval: 100000});


    $('.search-box-close .popup-close').click(function () {
        alert("test");
        $('.search-container').addClass("hide");
        $('.search-input').val("");
        $('.search-result-list .list-group-item').remove();

        /*if ($('.search-input').hasClass("find-centre")) {
            $('.search-input').removeClass("find-centre");
        } else if ($('.search-input').hasClass("search-database")) {
            $('.search-input').removeClass("search-database");
        }*/
    });

    $('.find-centre-btn').click(function () {
        $('.search-container').removeClass("hide");
        $('.search-input').attr('placeholder', 'Enter postcode or suburb');
        $('.search-input').addClass("find-centre");
    });

    $('.search-database-btn').click(function () {
        $('.search-container').removeClass("hide");
        $('.search-input').attr('placeholder', 'Enter blood type');
        $('.search-input').addClass("search-database");
    });

    $('.search-input').keyup(function () {
        if ($('.search-input').hasClass("find-centre")) {
            var key_words = $('.find-centre').val();
            $('.search-result-list').empty();
            $.ajax({
                type: "POST",
                url: "/bloodline/list_centre",
                data: {
                    'key_words': key_words
                },
                success: function (data) {
                    len = data.length;
                    if(len != 0) {
                        for (var i = data.length - 1; i >= 0; i--) {
                            $('.search-result-list').append('<li class="list-group-item">' + data[i] + '</li>');
                        }
                    }
                }
            });
            return false;
        } else if ($('.search-input').hasClass("search-database")) {
            var key_words = $('.search-database').val();
            $('.search-result-list').empty();
            $.ajax({
                type: "POST",
                url: "/bloodline/list_blood",
                data: {
                    'key_words': key_words
                },
                success: function (data) {
                    len = data.length;
                    if(len != 0) {
                        for (var i = data.length - 1; i >= 0; i--) {
                            $('.search-result-list').append('<li class="list-group-item">' + data[i] + '</li>');
                        }
                    }
                }
            });
            return false;
        }
    });
});