var app = angular.module('dashboard',[]).config(function($httpProvider) {
  $httpProvider.defaults.headers.post['X-CSRFToken'] = $('#csrftoken').val(); })

function dashboardCtrl($scope,$http,$location){
  NProgress.start();
  var tree_pacients = {};
  $scope.data = [{text: ''}];
  $scope.tpl = '/static/partials/list.html';
  $scope.pacients_tpl = '/static/partials/pacients.html';
  $scope.textarea = {focus:false};
  $scope.index = 0;
  $scope.data = [];
  $scope.pacients = [];
  $scope.pacient = {};

  $scope.safeApply = function(fn) {
    var phase = this.$root.$$phase;
    if(phase == '$apply' || phase == '$digest')
      this.$eval(fn);
    else
      this.$apply(fn);
  };

  $scope.setIndex = function(index){
    $scope.index = index;
  }

  $scope.change = function(index, question, focus){
    question.focus = true;
    $scope.index = index;
    var len = $scope.data.length;

    if(typeof focus === 'undefined'){
      focus = false;
    }

    if(len == 0){
      $scope.data.push({text:'', focus: focus});
    }else if( (question.text && $scope.data[len -1].text != '')){
      $scope.data.push({text:'', focus: focus});
    }else if(focus && index < len -1){
      $scope.data[index+1].focus = Math.random();
    }
  };

  $scope.backspace = function(index){
    var len = $scope.data.length;

    if($scope.data[index].text == ''){
      //delete item
      if(index != len -1){
        $scope.data.splice(index, 1);
      }
      //set focus
      if(len > 2){
        $scope.data[index -1].focus = true;
      }else{
        $scope.data[0].focus = true;
      }
    }
  }

  $scope.tab = function(index){
    $scope.textarea.focus = index + Math.random(); 
  }

  $scope.offFocus = function(question){
    question.focus = false;
    question.pid = $scope.pacient.id;

    $http.post('/question/update/',question).success(function(data){
      if(data.error === ""){
        question.id = data.id;
      }
    });
  }

  $scope.create_pacient = function(){
    $http.post('/pacient/update/', $scope.pacient).success(function(data){
      if(data.error === ""){
        $scope.pacient.id = data.id;
        $scope.change(0,{text:'foo'}, false);
      }
    });
  }

  $scope.hide_add_pacient = function(){
    $scope.add_pacient = false;
    if(typeof tree_pacients[$scope.pacient.id] === 'undefined'){
      tree_pacients[$scope.pacient.id] = $scope.pacient.id;
      $scope.pacients.push($scope.pacient);
    }
  }

  $scope.load_questions = function(uid){
    NProgress.start();
    var params = {
      uid: uid
    };

    $http.post('/question/list/', params).success(function(data){
      $scope.data = data;
      $scope.change(0,{text:'foo'}, true);
      NProgress.done();
    });
  }

  $http.post('/pacient/list/').success(function(data){
    $scope.pacients = data;
    angular.forEach(data, function(val, key){
      tree_pacients[val.id] = val.id;  
    });
    NProgress.done();
  });
}


app.directive('focusMe', function($timeout) {
  return {
    link: function(scope, element, attrs) {
      scope.$watch(attrs.focusMe, function(value) {
        if(value) { 
          element[0].focus();
        }
      });
    }
  };
});

app.directive('keyEnter', function($timeout) {
  return {
    link: function(scope, elm, attrs) {
      elm.bind('keydown', function (e) {
        var intKey = (window.Event) ? e.which : e.keyCode;
        switch(intKey) {
          case 13:
            scope.$apply(attrs.keyEnter);
            break;
          case 8:
            scope.$apply(attrs.backspace);
            break;
          case 9:
            e.preventDefault();
            scope.$apply(attrs.tab);
            return false;
            break;
        }
      });
    }
  };
});

app.directive('keyUp', function($timeout) {
  return {
    link: function(scope, elm, attrs) {
      elm.bind('keyup', function (e) {
        e.preventDefault();
        scope.$apply(attrs.keyUp);
      });
    }
  };
});

app.directive('onFocus', function($timeout) {
  return {
    link: function(scope, elm, attrs) {
      $(elm).bind('focus', function (e) {
        scope.safeApply(attrs.onFocus);
      });
    }
  };
});

app.directive('onBlur', function($timeout) {
  return {
    link: function(scope, elm, attrs) {
      $(elm).bind('blur', function (e) {
        scope.safeApply(attrs.onBlur);
      });
    }
  };
});
