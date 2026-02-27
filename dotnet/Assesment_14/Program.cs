using Assesment_14.Services;

var builder = WebApplication.CreateBuilder(args);

// Services
builder.Services.AddControllers();
builder.Services.AddEndpointsApiExplorer();

// Swagger
builder.Services.AddSwaggerGen();

// Custom services
builder.Services.AddSingleton<EmailService>();
builder.Services.AddSingleton<SmsService>();
builder.Services.AddHostedService<NotificationBackgroundService>();

var app = builder.Build();

// Enable Swagger for all environments (Assessment friendly)
app.UseSwagger();
app.UseSwaggerUI(c =>
{
    c.SwaggerEndpoint("/swagger/v1/swagger.json", "Assesment_14 API v1");
    c.RoutePrefix = "swagger";
});

app.UseHttpsRedirection();
app.UseAuthorization();

app.MapControllers();
app.Run();