angular.module("myApp").controller("registerController", function ($scope, AjaxService) {
    var user = {
        "name": $scope.username,
        "email": $scope.email,
        "password": $scope.password,
        "passwordRepeat": $scope.passwordRepeat
    };

    $scope.onRegister = function () {
        AjaxService.postRegister(user);
    };
});