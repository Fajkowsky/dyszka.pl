var myApp = angular.module("myApp", ["ngRoute", "ui.bootstrap"]);

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