try {
    let messagebird = require('messagebird')('iNExJakwOx2F2w37CzwWGi7aF')
} catch (error) {
    console.log(error)
}
console.log('hello world')
$('#submitBtn').click( function() {
    let msg = $('#messageText').val()
    console.log(msg);
    $('#chatContent').append(
        `<div class="card d-inline-flex bg-primary p-1 text-light">
        ${msg}
        </div>`
    )
});