const buttonOpen = document.getElementsByClassName('modalOpen')[0];
const modal = document.getElementsByClassName('modal')[0];
const buttonClose = document.getElementsByClassName('modalClose')[0];
const body = document.getElementsByTagName('body')[0];
// ボタンがクリックされた時
buttonOpen.addEventListener('click', function(){
  modal.style.display = 'block';
  console.log("push");
  body.classList.add('open');
});


// バツ印がクリックされた時
buttonClose.addEventListener('click',function(){
  modal.style.display = 'none';
  body.classList.remove('open');
});

// モーダルコンテンツ以外がクリックされた時
modal.addEventListener('click', function(){ 
    modal.style.display = 'none';
    body.classList.remove('open');
});