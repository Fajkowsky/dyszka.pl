var myApp = angular.module("myApp", ["ngRoute"]);

myApp.config(function ($routeProvider) {
    $routeProvider
        .when("/", {
            templateUrl: "templates/home.html",
            controller: "mainController"
        })
        .when("/login", {
            templateUrl: "templates/login.html",
            controller: "loginController"
        })
        .
        when("/register", {
            templateUrl: "templates/register.html",
            controller: "registerController"
        });
});

myApp.controller('mainController', function ($scope) {
    $scope.message = 'Everyone come and see how good I look!';
});

myApp.controller('loginController', function ($scope) {
    $scope.message = 'Look! I am an login page.';
});

myApp.controller('registerController', function ($scope) {
});