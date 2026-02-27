using Microsoft.AspNetCore.Mvc;

[ApiController]
[Route("api/[controller]")]
public class ProductController : ControllerBase
{
    private readonly ProductService _service;
    private readonly ILogger<ProductController> _logger;

    public ProductController(ProductService service, ILogger<ProductController> logger)
    {
        _service = service;
        _logger = logger;
    }

    [HttpGet]
    public IActionResult GetProducts()
    {
        _logger.LogInformation("Product list requested");
        return Ok(_service.GetProducts());
    }

    [HttpGet("error")]
    public IActionResult ThrowError()
    {
        throw new Exception("Test Exception");
    }
}