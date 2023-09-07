$(function(){
    document.querySelector("input").focus();
    document.querySelector(".enter-code").addEventListener("input", function({ target, data }){

    data && ( target.value = data.replace(/[^0-9]/g,'') );

    const hasValue = target.value !== "";
    const hasSibling = target.nextElementSibling;
    const hasSiblingInput = hasSibling && target.nextElementSibling.nodeName === "INPUT";

    if ( hasValue && hasSiblingInput ){

    target.nextElementSibling.focus();

    } 

    });
})