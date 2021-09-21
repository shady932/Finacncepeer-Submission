module.exports = {
    devServer: {
        inline: false,
        contentBase: "./financepeer",
    },
    module: {
        rules: [{
            test: /\.js$/,
            exclude: /node_modules/,
            use: {
                loader: "babel-loader"
            }
        }]
    }
}