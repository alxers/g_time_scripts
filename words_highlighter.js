function textNodesUnder(word){
  var n, walk=document.createTreeWalker(document.body,NodeFilter.SHOW_TEXT,null,false);
  while(n=walk.nextNode()) {
    // infinite loop ):
    if (n.textContent.match(word)) {
      var replacementNode = n.splitText(n.textContent.indexOf(word));
      var sp = document.createElement('span');
      sp.style.fontWeight = 900;
      sp.appendChild(document.createTextNode('==!!!=='));
      n.parentNode.insertBefore(sp, replacementNode);
    }
  }
  return 0;
}
