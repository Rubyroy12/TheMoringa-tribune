<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>


    <nav class="navbar navbar-inverse">
        <div class="container-fluid">
            <div class="navbar-header">
                <a class="navbar-brand" href="{% url 'newsToday' %}">The Moringa Tribune</a>
            </div>

            <!-- Adding a search form  -->
            <div class="col-sm-4 col-md-4 navbar-right">

                <form class="navbar-form" role="search" action="{% url 'search_results' %}">

                    <div class="input-group">
                        <input type="text" class="form-control" placeholder="Search Article" name="article">
                        <div class="input-group-btn">
                            <button class="btn btn-default" type="submit"><i
                                    class="glyphicon glyphicon-search"></i></button>
                        </div>
                    </div>

                </form>
            </div>
            <!-- search form end -->
        </div>
    </nav>
</body>

</html>