using Microsoft.AspNetCore.Identity;

namespace Assesment_12.Models
{
    public class ApplicationUser : IdentityUser
    {
        public string? Department { get; set; }
    }
}