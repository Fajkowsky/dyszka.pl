angular.module("myApp").service("AjaxService", function ($http) {
    //get sample
    this.getProducts = function () {
        return $http.get("/products");
    };

    this.postTest = function (data) {
        return $http.post("/user", data);
    };
});