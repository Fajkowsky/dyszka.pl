angular.module("myApp").controller("registerController", function ($scope, AjaxService) {
    $scope.user = {
        "name": "",
        "email": "",
        "password": "",
        "passwordRepeat": ""
    };

    $scope.onRegister = function () {
        AjaxService.postRegister($scope.user);
    };
});