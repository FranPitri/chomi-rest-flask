$(function () {

    $('#fetchbtn').click(onTracklistButtonClick)

    function onTracklistButtonClick() {
        $.get(
            'http://localhost:5000/api/tracks/',
            function (data) {
                data.forEach(function (e) {
                    console.log(e)
                    $('#tracklist').append(
                        $('<a>')
                            .addClass('collection-item waves-effect')
                            .attr('data-id', e.id)
                            .html(e.name)
                    )
                })
            }
        )
    }

})