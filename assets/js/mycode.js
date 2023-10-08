const fooditems = document.querySelectorAll('.food .item');
fooditems.forEach((fooditem) => {
    fooditem.addEventListener('mouseover', function (event) {
        var foodfront = fooditem.querySelector('.front');
        var foodback = fooditem.querySelector('.back');
        foodback.classList.remove('hidden');
        foodfront.classList.add('hidden');
    });
    fooditem.addEventListener('mouseleave', function (event) {
        var foodfront = fooditem.querySelector(".front");
        var foodback = fooditem.querySelector(".back");
        foodback.classList.add('hidden');
        foodfront.classList.remove('hidden');
    });
  });


 