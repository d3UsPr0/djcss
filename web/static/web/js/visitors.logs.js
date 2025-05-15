$(function () {
    var client = new ClientJS(); // Create A New Client Object

    var url = $('#base_url').val() + "api/visitorsLog";

    $.ajaxSetup({
                headers: {
                    'X-CSRF-TOKEN': $('meta[name="csrf-token"]').attr('content')
                }
            });

    var data = {
        browserId: client.getFingerprint(),
        browserName: client.getBrowser(),
        browserVersion: client.getBrowserVersion(),
        userAgent: client.getUserAgent(),
        os: client.getOS(),
        osVersion: client.getOSVersion(),
    };


    $.ajax({
        type: "GET",
        url: url,
        data: data,
        dataType: 'json',
        success: function (response) {
            //console.log(response);
            var visitors = response;
            $('#today').html(visitors.today);
            $('#yesterday').html(visitors.yesterday);
            $('#week').html(visitors.week);
            $('#month').html(visitors.month);
            $('#all').html(visitors.all);
        },
        error: function (err, msg) {
            console.log(err, msg);
        }
    });


});