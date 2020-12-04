
  var headersList = {}
  var nRequests = 0


  function getCacheTime(url,element) {
    var request = {
      'url': url,
      'success': function(data, textStatus, jqXHR) {
        nRequests = nRequests + 1;
        var headers = jqXHR.getAllResponseHeaders();
        headersList[element] = headers;


      },
      'complete': function(data) {
        if(nRequests == Object.keys(urls).length) {
          console.log(headersList);
          $.ajax({

             type: "GET",
             url: "/getDates",
             data: 'headers='+JSON.stringify(headersList),
             success: function(data){
              console.log(data)
              insertInTable(data);


             },
         });
        }
      }
    }


    $.ajax(request);
    
  }

const urls = {{links|safe}};

  for(var element in urls) {
    getCacheTime(urls[element],element);
  }
