using Microsoft.Extensions.Caching.Memory;

public class ProductService
{
    private readonly IMemoryCache _cache;
    private readonly ILogger<ProductService> _logger;

    public ProductService(IMemoryCache cache, ILogger<ProductService> logger)
    {
        _cache = cache;
        _logger = logger;
    }

    public List<Product> GetProducts()
    {
        if (!_cache.TryGetValue("productList", out List<Product> products))
        {
            _logger.LogInformation("Fetching from DB (Simulated)");

            products = new List<Product>
            {
                new Product { Id = 1, Name = "Laptop" },
                new Product { Id = 2, Name = "Mobile" }
            };

            _cache.Set("productList", products, TimeSpan.FromMinutes(5));
        }

        return products;
    }
}