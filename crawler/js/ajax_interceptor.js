// This js wrapps the open function from XMLHttpRequest 
callbackWrap(XMLHttpRequest.prototype, 'open', 0, XMLHTTPObserverOpen);
callInterceptionWrapper(XMLHttpRequest.prototype, 'send', 0, XMLHTTPObserverSend);