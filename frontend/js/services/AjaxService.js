angular.module("myApp").service("AjaxService", function ($http, $location) {
    var url = "http://127.0.0.1:8000";

    this.postTest = function (data) {
        return $http.post(url + "/user/", data);
    };

    this.postRegister = function (data) {
        return $http.post(url + "/register/", data).success(
            function (data) {
                console.log(data);
                data = angular.toJson(data);
                console.log("powinnen być JSON" + data);

                if (data.status === "True") {
                    $location.path("/");
                } else {
                    console.log("error");
                    return (data.msg);
                }
            });
    };
});