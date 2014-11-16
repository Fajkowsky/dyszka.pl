angular.module("myApp").service("AjaxService", function ($http) {
    var url = "http://127.0.0.1:8000/";

    this.postTest = function (data) {
        return $http.post(url + "/user", data);
    };

    this.postRegister = function (data) {
        return $http.post(url + "/register", data).success(
            function (data) {
                console.log(data);
            });
    };
});