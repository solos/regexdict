var RegexDictCtrl = function($scope, $element){
$scope.description = '';
$scope.$watch('word',
    function(to, from){
        var filter = new RegExp(to);
        //var filter = eval('/' + to + '/');
        var count = 0;
        var wordlist = {};
        for (i in dict){
            if (count < 50) {
                if (filter.test(i)){
                    wordlist[i] = dict[i];
                    count += 1;
                }
            }
        };
        $scope.description = wordlist;
    })
};
//angular.bootstrap(document.documentElement);
//angular.module('RegexDict', [], function(){console.log('here')});
angular.module('RegexDict', []);
