// add to cart programs starts here
$('.addtocart').click(function(){
    let product_id=$(this).attr("product_id").toString()
    console.log(product_id)
    // let token=$('input[name=csrfmiddlewaretoken]')
    $.ajax({
        method: "POST",
        url: "/add-to-cart",
        data: {
            'product_id':product_id,
            // csrfmiddlewaretoken:token
        },
        dataType: "dataType",
        success: function (data) {
            document.getElementById('message').innerHTML=data.data
        }
    });
})




// quantity increasing programs starts here
$('.increase').click(function(){
    let id = $(this).attr("pid").toString()
    let eml = this.parentNode.children[2]
    $.ajax({
        type:"GET",
        url:"/increase-quantity",
        data:{
            prod_id:id
        },
        success: function(data){
            eml.innerText=data.quantity
            document.getElementById('amount').innerText=data.amount
        }
    })
})



// quantity decreasing programs starts here
$('.decrease').click(function(){
    let id = $(this).attr("pid").toString()
    let eml = this.parentNode.children[2]
    $.ajax({
        type:"GET",
        url:"/decrease-quantity",
        data:{
            prod_id:id
        },
        success: function(data){
            eml.innerText=data.quantity
            document.getElementById('amount').innerText=data.amount
        }
    })
})



// quantity removing programs starts here
$('.remove-quantity').click(function(){
    let id = $(this).attr("pid").toString()
    let eml = this
    console.log(id)
    $.ajax({
        type:"GET",
        url:"/remove-quantity",
        data:{
            prod_id:id
        },
        success: function(data){
            // eml.innerText=data.quantity
            document.getElementById('amount').innerText=data.amount
            eml.parentNode.parentNode.parentNode.parentNode.remove()
        }
    })
})



