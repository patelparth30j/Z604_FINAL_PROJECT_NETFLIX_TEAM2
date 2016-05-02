/**
 * 
 */
	    var str = 'get "something" from "any site"';
	    var tokens = [].concat.apply([], str.split('"').map(function(v,i){
	       return i%2 ? v : v.split(' ')
	    })).filter(Boolean);