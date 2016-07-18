var app = angular.module('myApp', ['ngRoute']);


app.config(function($routeProvider){
    $routeProvider

    .when('/login', {
        templateUrl : 'static/templates/login.html',
        controller : 'LoginController',
    })

    .when('/signup', {
        templateUrl : 'static/templates/signup.html',
        controller : 'SignUpController',
    })

    .when('/profile', {
        templateUrl : 'static/templates/profile.html',
        controller : 'ProfileController',
    });

});


app.controller('SignUpController', function($scope, $http){

    $scope.signUp = function()
    {
        var user={}
        user.username = $scope.username
        user.email = $scope.email
        user.password = $scope.pass
        console.log(user.data);

        var url = 'http://localhost:8000/authenticate_api/registration-api/';
        $http.post(url, user).success(function(result){
            console.log("success", result);
            //$scope.userInfo = result;
        }).error(function(err) {
        console.log('err', err);
       });

    }//signup function
});


app.controller("LoginController", function($scope, $http, $window){

    $scope.login=function()
    {
        $scope.success =0;
        var user = {};
        user.email = $scope.email;
        user.password = $scope.pass;

        //Hit post request with required param and Url
        var url = 'http://localhost:8000/authenticate_api/login-api/';
        $http.post(url, user).success(function(result){
            localStorage.setItem('token',result.token);
            window.location.href ='#/profile';
            }).error(function(err) {
                console.log('err', err);
            });
    } //ends login()
});


app.controller('ProfileController', function($scope, $http){

    var token = localStorage.getItem('token');
    var config = {headers: {'Authorization': 'Token '+token} };
    var url = 'http://localhost:8000/authenticate_api/profile-api/'

    $http.get(url, config).success(function(result){
        $scope.userInfo = result;
        $scope.profile_pic = 'http://1.bp.blogspot.com/-RElhgIdCr8s/T_2vbvEZWGI/AAAAAAAAC00/4lAIcWSYw80/s1600/Passport6.png';
    }).error(function(err) {
    console.log('err', err);
   });

    $scope.imgPopup = function(file)
    {
        var url ='http://localhost:8000/authenticate_api/profile-image-api/'
        var config = {headers: {'Authorization': 'Token '+token} };
        var profile_pic = file;

        $http.put(url, profile_pic, config).success(function(result){
           $scope.profile_pic = result.profile_pic;
           alert(result.profile_pic);
        });
    };

});
