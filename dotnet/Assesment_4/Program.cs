using Assesment_4.Middleware;
using Assesment_4.Services;

var builder = WebApplication.CreateBuilder(args);

// Add MVC
builder.Services.AddControllersWithViews();

// Register custom service (Dependency Injection)
builder.Services.AddScoped<IMyService, MyService>();

var app = builder.Build();

// Use custom middleware
app.UseMiddleware<RequestLoggingMiddleware>();

app.UseStaticFiles();
app.UseRouting();

// Default routing
app.MapControllerRoute(
    name: "default",
    pattern: "{controller=Home}/{action=Index}/{id?}");

app.Run();
