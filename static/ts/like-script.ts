
interface Button
{
    id: number
    text: string
    count: number
}

$(".liker__vote-button").on("click", function(e) {
    let $parent = $(this).parent()
    $.ajax({
        method: $parent.attr("method"),
        url: $parent.attr("action"),
        data: `${$parent.serialize()}&val=${$(this).attr("value")}`
    })
    .done((data: Button) => {                           // POST returns a JSONResponse, and JQuery automatically parses JSON
        $parent.find(".liker__likes").text(data.count)         // Probs something about MIME types
        $parent.find("button").prop("disabled", false)
    })
    $parent.find("button").prop("disabled", true)
})
