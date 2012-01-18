_.mixin({
    subclass:  function(child, parent) {
        var hasProp = Object.prototype.hasOwnProperty;
        for (var key in parent) {
            if (hasProp.call(parent, key)) child[key] = parent[key];
        }
        function ctor() {
            this.constructor = child;
        }

        ctor.prototype = parent.prototype;
        child.prototype = new ctor;
        child.__super__ = parent.prototype;
        return child;
    },
    pad: function(n) {
        return n < 10 ? '0' + n : n;
    },
    formatDjangoDate: function(date_string) {
        var z = new Date(date_string);

        return (z.getMonth() + 1) + '/' + z.getDate() + '/' + z.getFullYear();
    },
    formatDjangoTime: function(date_string) {
        var z = new Date(date_string),
            hrs = z.getHours(),
            time_str = '';

        if (hrs === 0) {
            time_str += '12';
        } else if (hrs > 12) {
            time_str += hrs - 12;
        } else {
            time_str += hrs;
        }

        time_str += ':' + _.pad(z.getMinutes());

        if (hrs < 12) {
            time_str += 'am';
        } else {
            time_str += 'pm';
        }
        return time_str;
    },
    isValidDate: function(date) {
        var pattern = /^[0-9]{1,2}\/[0-9]{1,2}\/[0-9]{4}$/;
        if (date.match(pattern)) return true;
        return false;
    },
    isValidNumber: function(number) {
        var pattern = /^[0-9\.]+$/;
        if (number.match(pattern)) return true;
        return false;
    },
    isValidPositiveNumber: function(number) {
        var pattern = /^[0-9\.]+$/;
        if (number.match(pattern) && Math.abs(parseFloat(number)) > 0.00001) return true;
        return false;
    },
    isValidTime: function(time) {
        var pattern = /^[0-9]{1,2}\:[0-9]{2}[am|pm]/;
        if (time.match(pattern)) return true;
        return false;
    }
});

_.templateSettings = {
  'interpolate': /\{\{(.+?)\}\}/g
}

