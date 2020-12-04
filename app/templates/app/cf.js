var YourID = 0

var headersList = {};
var nRequests = 0


function getCacheTime(url,element) {
  var request = {
    'url': url,
    'type':"GET",
    'success': function(data, textStatus, jqXHR) {
      nRequests = nRequests + 1;
      var headers = jqXHR.getAllResponseHeaders();
      headersList[element] = headers;
    },
    'complete': function(data) {
      if(nRequests == Object.keys(urls).length) {
        $.ajax({

           type: "GET",
           url: "/getID",
           data: 'headers='+JSON.stringify(headersList),
           success: function(data){
            $('#personID').html(data);
            YourID = data;


           },
       });
      }
    }
  }


  $.ajax(request);
  
}


  const urls = {{res|safe}};

  for(var element in urls) {
    getCacheTime(urls[element],element);
  }
  console.log(headersList);
