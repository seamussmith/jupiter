
interface Button
{
    id: number
    text: string
    count: number
}

$(".vote-button").on("click", function(e) {
    let $parent = $(this).parent()
    $.ajax({
        method: $parent.attr("method"),
        url: $parent.attr("action"),
        data: `${$parent.serialize()}&val=${$(this).attr("value")}`
    })
    .done((data: Button) => {   // POST returns a JSONResponse, and JQuery automatically parses JSON
        $parent.find(".likes").text(data.count)
        $parent.find("button").prop("disabled", false)
    })
    $parent.find("button").prop("disabled", true)
})
