var app = angular.module('myApp', ['ngFileUpload']);


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


app.controller("LoginController", function($scope, $http, Upload){

    $scope.login=function()
    {
        $scope.success =0;
        var user = {};
        user.email = $scope.email;
        user.password = $scope.pass;

        //Hit post request with required param and Url
        var url = 'http://localhost:8000/authenticate_api/login-api/';
        $http.post(url, user).success(function(result){

            var url = 'http://localhost:8000/authenticate_api/profile-api/'
            var config = {headers: {'Authorization': 'Token '+result.token}}
            localStorage.setItem('token',result.token);
            //hit Get API to get profile data of logged in user
            $http.get(url, config).success(function(result){

                $scope.success =1;
                console.log(result);
                var key = Object.keys(result);
                var value = [];
                for (i=0; i<key.length; i++){
                    value.push(result[key[i]]);
                    localStorage.setItem(key[i], value[i]);
                }
                console.log(localStorage);
                $scope.username = result.username;
                $scope.contact_no = result.contact_no;
                $scope.profile_pic = result.profile_pic
                //                $scope.profile_pic = 'http://10721-presscdn-0-80.pagely.netdna-cdn.com/wp-content/uploads/2008/08/winding-path.jpg'
                //                $scope.profile_pic = '/home/zenga/Videos/a.mp4'
            });

        }).error(function(err) {
        console.log('err', err);
        });

    } //ends login()


    $scope.imgPopup = function(file)
    {
        var url ='http://localhost:8000/authenticate_api/profile-image-api/'
        var token = localStorage.getItem('token');
        var config = {headers: {'Authorization': 'Token '+token} };
        var profile_pic = file;

        $http.put(url, profile_pic, config).success(function(result){
           $scope.profile_pic = result.profile_pic;
           alert(result.profile_pic);
        });
    };
});


app.controller('ProfileController', function($scope){
    $scope.profile = function()
    {
//        $scope.email = localStorage.getItem("email");
//        $scope.gender = localStorage.getItem("gender");
//        $scope.phone = localStorage.getItem("contact_no");
//        $scope.profile_pic = localStorage.getItem("profile_pic");
    }

});