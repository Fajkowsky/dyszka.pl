angular.module("myApp").controller("loginController", function ($scope, AjaxService) {
    var user = [
        {username: "James", password: "testP"}
    ];

    $scope.onLogin = function () {
        AjaxService.postTest(user);
    };
});