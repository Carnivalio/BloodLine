$(document).ready(function () {
    $('#myCarousel').carousel({interval: 100000});
    var myDate = new Date();
//获取当前年
var year=myDate.getFullYear();
//获取当前月
var month=myDate.getMonth()+1;
//获取当前日
var date=myDate.getDate();
var h=myDate.getHours();       //获取当前小时数(0-23)
var m=myDate.getMinutes();     //获取当前分钟数(0-59)
var s=myDate.getSeconds();

var now=year+'-'+p(month)+"-"+p(date);
    $('#from_date_picker').val(now);
    alert($('#from_date_picker').val());

    $('.search-box-close').click(function () {
        $('.search-container').addClass("hide");
        if ($('.search-input').hasClass("find-centre")) {
            $('.search-input').removeClass("find-centre");
        } else if ($('.search-input').hasClass("search-database")) {
            $('.search-input').removeClass("search-database");
        }
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
        var key_words = $('.find-centre').val();
        $('.search-result-list').empty();
        $.ajax({
            type: "POST",
            url: "../bloodline/list_centre/",
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
    });





});