// Progress Bar:
$(window).on('beforeunload', function () {
    $('body').hide();
    $(window).scrollTop(0);
});

window.onscroll = function () {
    progressBar()
};

function progressBar() {
    var winScroll = document.body.scrollTop || document.documentElement.scrollTop;
    var height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
    var scrolled = (winScroll / height) * 100;
    document.getElementById("myBar").style.width = scrolled + "%";
    console.log("Window Scrolling")
}

var controller;

// -- Menu Functionality:
console.log("Beginning: I'm here!")
function myFunction() {
  var x = document.getElementById("navbar_id");
  if (x.className === "navbar") {
    x.className += " responsive";
  } else {
    x.className = "navbar";
  }
}

// // Scroll Animations--
// var controller;
//
// // Home Page Animations ---------------------------------------------------------------------------
// $(function () {
//     //controller
//     controller = new ScrollMagic.Controller();
//
//     //slide
//   if ($(window).width() > 480) {
//     var tween = new TimelineMax().fromTo("#introSlogan", 1, {
//         left: 0
//     }, {
//         left: "40%",
//     });
//
//     var scene1 = new ScrollMagic.Scene({
//             triggerElement: '#introSlogan'
//         })
//         .setTween(tween).addTo(controller);
//   }
//
//     var tween2 = new TimelineMax().fromTo("body", 1, {
//         background: "linear-gradient(90deg, #1b2735 0%, #090a0f 100%)"
//     }, {
//         background: "linear-gradient(90deg, #4b6cb7 0%, #182848 100%)"
//     });
//
//     // var scene2 = new ScrollMagic.Scene({
//     //         triggerElement: '#technical-work-title'
//     //     })
//     //     .setTween(tween2).addTo(controller);
//
// });
