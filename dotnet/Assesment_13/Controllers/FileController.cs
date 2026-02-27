using Microsoft.AspNetCore.Mvc;

[ApiController]
[Route("api/[controller]")]
public class FileController : ControllerBase
{
    private readonly ILogger<FileController> _logger;
    private readonly string _path = Path.Combine(Directory.GetCurrentDirectory(), "Uploads");

    public FileController(ILogger<FileController> logger)
    {
        _logger = logger;

        if (!Directory.Exists(_path))
            Directory.CreateDirectory(_path);
    }

    [HttpPost("upload")]
    public async Task<IActionResult> Upload(IFormFile file)
    {
        if (file == null || file.Length == 0)
            return BadRequest("No file uploaded");

        var filePath = Path.Combine(_path, file.FileName);

        using var stream = new FileStream(filePath, FileMode.Create);
        await file.CopyToAsync(stream);

        _logger.LogInformation("File uploaded: {FileName}", file.FileName);

        return Ok("File uploaded successfully");
    }

    [HttpGet("download/{fileName}")]
    public IActionResult Download(string fileName)
    {
        var filePath = Path.Combine(_path, fileName);

        if (!System.IO.File.Exists(filePath))
            return NotFound();

        var bytes = System.IO.File.ReadAllBytes(filePath);
        _logger.LogInformation("File downloaded: {FileName}", fileName);

        return File(bytes, "application/octet-stream", fileName);
    }
}