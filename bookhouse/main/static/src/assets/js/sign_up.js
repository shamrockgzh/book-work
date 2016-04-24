(function(window, angular, undefined) {'use strict';


    var signUpApp = angular.module('bookhouse.main.app.signUp', []);


    signUpApp.controller('signUpCtrl', ['$scope', '$http', function($scope, $http) {
        $scope.user_name = null;
        $scope.user_password = null;


        $scope.Mysubmit=function() {
            $http({
                method: 'POST',
                url: '/api/account/sign-up/',
                data: {
                    'user_name': $scope.user_name,
                    'user_password': $scope.user_password
                }
            }).success(function (data, status, headers, config) {

                ipCookie('access_token', data['token'], {path: '/', expires: 14});
                ipCookie('access_name', data['name'], {path: '/', expires: 14});
                alert(data['time']);
                $window.location = '/success/'
            }).error(function (data, status, headers, config) {

            });
        };
    }]);

})(window, window.angular);
