angular.module("myApp").controller("registerController", function ($scope, AjaxService) {
    $scope.user = {
        "username": "",
        "email": "",
        "password": "",
        "password2": ""
    };

    $scope.onRegister = function () {
        AjaxService.postRegister($scope.user);
    };
});
