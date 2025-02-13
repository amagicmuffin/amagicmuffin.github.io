module.exports = function (eleventyConfig) {
    const months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];
    eleventyConfig.addPassthroughCopy("./src/CNAME")
    eleventyConfig.addPassthroughCopy("./src/*.css")
    eleventyConfig.addPassthroughCopy("./src/*.js")
    eleventyConfig.addPassthroughCopy("./src/assets/*")
    eleventyConfig.addPassthroughCopy("./src/assets/*/*")
    // eleventyConfig.addPassthroughCopy("./src/blog/*")
    eleventyConfig.addPassthroughCopy("./src/blog/*/*")
    // eleventyConfig.addPassthroughCopy("**/*.pdf");
    eleventyConfig.addFilter("formatDate", function(date) {
        return `${date.getDate()} ${months[date.getMonth()]} ${date.getFullYear()}`;
    });
    
    return {
        dir: {
            input: "src",
            output: "docs",
        }
    }
}