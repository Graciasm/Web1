var Links = {
  SetColor: function(color) {
    // var alist = document.querySelectorAll('a');
    // var i = 0;
    // while (i < alist.length) {
    //   alist[i].style.color = color;
    //   i = i + 1;
    // }
    $('a').css('color', color);
  }
}
var Body = {
  SetColor: function(color) {
    document.querySelector('body').style.color = color;
  },
  SetBackgroundColor: function (color) {
    document.querySelector('body').style.backgroundColor = color;
  }
}

function BodySetColor(color) {
  document.querySelector('body').style.color = color;
}

function BodySetBackgroundColor(color) {
  document.querySelector('body').style.backgroundColor = color;
}

function night_day_handler(self) {
  var target = document.querySelector('body');
  if (self.value === 'night') {
    Body.SetBackgroundColor('black');
    Body.SetColor('white');
    self.value = 'day';
    Links.SetColor('powderblue');
  } else {
    Body.SetBackgroundColor('white');
    Body.SetColor('black');
    self.value = 'night';
    Links.SetColor('blue');
  }
}
/* 네비에서 현재패이지를 강조하려고 했으나 실패
function Currentpage_Underline(){
  var sidelinklist = document.getElementById('sidebar').querySelectorAll('ol li a');
  var j = 0;
  while(j<sidelinklist.length){
    var temphref = sidelinklist[j].getAttribute("href");
    if(temphref === window.location.href){
      sidelinklist[j].style.textDecoration="underline";
    }
    j=j+1;
  }
}*/
