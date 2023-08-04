// This is just notes! Not actually working JS file!
// companies_page.html
window.onload = () => {
    var div_content = document.getElementById('content');
    var request = new XMLHttpRequest();

    request.onreadystatechange = function() {
        if (request.readyState == 4) {
            var response = JSON.parse(request.responseText);
            var companies = response['companies'];

            for (var company of companies) {
//                var header = document.createElement('h1');
//                header.innerHTML = company['name'];
//                header.id = company['id'];
//
//                div_content.appendChild(header);

                var url = "'company_detail/" + company['id'] + "'";
                div_content.innerHTML += '<h2>' + company['name'] + ' <button onclick="location.href=' + url + '">More Info</button></h2>';
                div_content.innerHTML += '<p>' + company['country'] + '</p>';
            }
        }
    }

    request.open('get', '{% url 'companies_api_url' %}', true);
    request.send()
}
// ---------------------------------COMPANIES PAGE ENDS--------------------------------
// Company Detail Page
window.onload = () => {
    var company_id = location.href.split('/').slice(-1);
    var div_content = document.getElementById('content');
    var request = new XMLHttpRequest();

    request.onreadystatechange = function() {
        if (request.readyState == 4) {
            var response = JSON.parse(request.responseText);
            var company = response['company'];

            div_content.innerHTML += "<h1>" + company['name'] + "</h1>";
        }
    }

    request.open('get', "{% url 'company_detail_api_url' %}?company_id=" + company_id, true);
    request.send()
}
