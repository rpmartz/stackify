
technologies = {
    'A': ['Angular.js', 'Apache', 'Agda', 'Accumulo', 'ArangoDB'],
    'B': ['Backbone.js', 'Bootstrap', 'Brython'],
    'C': ['C++', 'C#', 'Coldfusion', 'Clojure', 'Couchbase', 'Cassandra', 'CentOS'],
    'D': ['Dart', 'D', 'Django', 'Docker', 'DynamoDB', 'Dojo.js', 'Debian'],
    'E': ['Ember.js', 'Erlang', 'Elm', 'Elixir', 'Express.js'],
    'F': ['F#', 'Flask', 'Frege', 'FoundationDB', 'Fedora', 'Foxx'],
    'G': ['Go', 'Grunt.js', 'Gulp.js', 'Gentoo'],
    'H': ['Haskell', 'Hadoop', 'Hapi.js', 'Hive', 'HyperDex', 'HBase'],
    'I': ['Io.js', 'Idris', 'Io', 'InfluxDB'],
    'J': ['Julia', 'Java', 'Jython', 'JRuby', 'jQuery'],
    'K': ['Knockout.js', 'Kotlin', 'Kinesis', 'Kubuntu'],
    'L': ['Linux', 'Lisp', 'Lua', 'Laravel'],
    'M': ['Marionette.js', 'MongoDB', 'MySQL', 'MariaDB', 'Memcached'],
    'N': ['Node.js', 'Neo4J'],
    'O': ['OCaml', 'Oracle', 'Objective C'],
    'P': ['Phoenix', 'Postgres', 'Python', 'Pig'],
    'Q': ['Qubes'],
    'R': ['Ruby', 'R', 'Rust', 'RethinkDB', 'RavenDB', 'Riak', 'Redis', 'Red Hat'],
    'S': ['Scala', 'Spring', 'Sqlite', 'SQL Server', 'Swift', 'Smalltalk', 'Spark'],
    'T': ['Tcl', 'Tomcat'],
    'U': ['Ubuntu', 'UNIX'],
    'V': ['Vagrant', 'Vert.x', 'Visual Basic'],
    'W': ['Wordpress', 'Windows'],
    'X': ['XML', 'XSLT', 'Xubuntu'],
    'Y': ['YARN'],
    'Z': ['Zookeeper', 'Zuul'],
}

from random import randint


def get_stack_for_letter(letter):
    potential_technologies = technologies[letter]
    num_technologies = len(potential_technologies)
    idx = randint(0, num_technologies - 1)

    return potential_technologies[idx]
