import '../styles/index.scss';

$('.btn').click(function(){
  $.ajax({
    url: "http://127.0.0.1:8000/api-token/course/",
  }).done(function(data) {
      console.log(data)
  });
})
