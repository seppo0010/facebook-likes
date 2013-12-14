var FB = require('fb');
var fs = require('fs');

FB.setAccessToken(process.argv[2]);

FB.api('me/friends', {
  fields: 'id',
  fields: 'birthday'
}, function(res) {
  res.data.forEach(function(val, idx) {
    fs.writeFileSync('data/' + val.id + '.birthday', JSON.stringify(val));
    FB.api(val.id + '/likes', function(res) {
      fs.writeFileSync('data/' + val.id + '.likes', JSON.stringify(res));
    });
    FB.api(val.id, {fields: 'languages'}, function(res) {
      fs.writeFileSync('data/' + val.id + '.languages', JSON.stringify(res));
    });
  });
});
