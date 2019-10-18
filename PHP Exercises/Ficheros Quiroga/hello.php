<html>
 <?php $s = "hola mundo"; ?>
 <?=$s = "adios"; ?>
 <head>
  <title>PHP Test</title>
 </head>
 <body>
    <?php echo '<p>Hello World</p>'; ?>
    <p>Hello, today is <?=date('l, F jS, Y'); ?>.</p>

    <p>Hello, <?=$s; ?>.</p>

    <p>Hello, <?"hola"; ?>.</p>

 </body>
</html>
