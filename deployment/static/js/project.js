(function(){jQuery(document).ajaxSend(function(t,e,o){var n,c,i,u,l,r
r=o.type,/^(GET|HEAD|OPTIONS|TRACE)$/.test(r)||(n=o.url,c=document.location.host,i=document.location.protocol,n!=(l=i+(u="//"+c))&&n.slice(0,l.length+1)!=l+"/"&&n!=u&&n.slice(0,u.length+1)!=u+"/"&&/^(\/\/|http:|https:).*/.test(n))||e.setRequestHeader("X-CSRFToken",function(t){var e,o,n,c=null
if(document.cookie&&""!=document.cookie)for(e=document.cookie.split(";"),o=0;o<e.length;o++)if((n=jQuery.trim(e[o])).substring(0,t.length+1)==t+"="){c=decodeURIComponent(n.substring(t.length+1))
break}return c}("csrftoken"))})}).call(this)
